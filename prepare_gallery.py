#!/usr/bin/env python3
"""Offline photo preparation: thumbnails, viewing copies, album ZIPs and URL manifest."""
import argparse, hashlib, json, math, re, zipfile
from pathlib import Path
from urllib.parse import quote, urlsplit

def main():
    parser=argparse.ArgumentParser(description='Prepare local photos for an external public HTTPS storage bucket.')
    parser.add_argument('--source',required=True,help='Folder containing original photos; subfolders become albums')
    parser.add_argument('--output',required=True,help='New folder for thumbnails, viewing photos, ZIPs and manifest')
    parser.add_argument('--base-url',required=True,help='Public HTTPS bucket/domain URL, e.g. https://photos.example.com')
    parser.add_argument('--zip-mb',type=int,default=1024,help='Approximate maximum uncompressed bytes per album ZIP part, in MiB')
    parser.add_argument('--no-zips',action='store_true',help='Skip album ZIP generation')
    args=parser.parse_args();source=Path(args.source).resolve();output=Path(args.output).resolve();base=args.base_url.rstrip('/')
    url=urlsplit(base)
    if url.scheme!='https' or not url.netloc or url.username or url.password or url.query or url.fragment:parser.error('Base URL must be a public HTTPS URL without credentials, query or fragment.')
    if not source.is_dir():parser.error('Source folder does not exist.')
    if source==output or source in output.parents or output in source.parents:parser.error('Output must be a separate folder outside the source tree.')
    if output.exists() and any(output.iterdir()):parser.error('Output folder must be empty to avoid overwriting files.')
    if args.zip_mb<=0:parser.error('--zip-mb must be positive.')
    try:
        from PIL import Image,ImageOps
    except ImportError:raise SystemExit('Install Pillow first: python -m pip install Pillow')
    (output/'thumbs').mkdir(parents=True,exist_ok=True);(output/'views').mkdir();(output/'archives').mkdir()
    extensions={'.jpg','.jpeg','.png','.webp','.gif','.bmp','.tif','.tiff'}
    paths=sorted(p for p in source.rglob('*') if p.is_file() and p.suffix.lower() in extensions)
    photos=[];albums={};failures=[]
    for i,path in enumerate(paths,1):
        relative=path.relative_to(source).as_posix();album=path.parent.relative_to(source).as_posix();album='Ảnh lớp' if album=='.' else album
        ident=hashlib.sha256(relative.encode()).hexdigest()[:24]
        try:
            with Image.open(path) as image:
                image=ImageOps.exif_transpose(image);image.thumbnail((1800,1800))
                if image.mode not in ('RGB','L'):
                    rgba=image.convert('RGBA');rgb=Image.new('RGB',rgba.size,'white');rgb.paste(rgba,mask=rgba.getchannel('A'));image=rgb
                else:image=image.convert('RGB')
                image.save(output/'views'/f'{ident}.jpg',quality=85,optimize=True)
                image.thumbnail((480,480));image.save(output/'thumbs'/f'{ident}.jpg',quality=78,optimize=True)
            photos.append({'name':path.name,'caption':'','album':album,'size':path.stat().st_size,'thumbnail':base+f'/thumbs/{ident}.jpg','full':base+f'/views/{ident}.jpg','original':base+'/originals/'+quote(relative,safe='/')})
            albums.setdefault(album,[]).append(path)
            print(f'[{i}/{len(paths)}] {relative}')
        except Exception as error:
            failures.append({'file':relative,'error':str(error)});print(f'SKIP {relative}: {error}')
    archives=[]
    if not args.no_zips:
        limit=args.zip_mb*1024*1024
        for album,items in albums.items():
            groups=[];group=[];size=0
            for path in items:
                length=path.stat().st_size
                if group and size+length>limit:groups.append(group);group=[];size=0
                group.append(path);size+=length
            if group:groups.append(group)
            ident=hashlib.sha256(album.encode()).hexdigest()[:16]
            for part,group in enumerate(groups,1):
                filename=f'{ident}-{part:03}.zip'
                with zipfile.ZipFile(output/'archives'/filename,'w',zipfile.ZIP_STORED,allowZip64=True) as z:
                    for path in group:z.write(path,path.relative_to(source).as_posix())
                archives.append({'album':album,'name':album+(f' · phần {part}/{len(groups)}' if len(groups)>1 else ''),'url':base+'/archives/'+filename})
                print('ZIP:',filename)
    manifest={'photos':photos,'slides':[],'downloads':{'allUrl':'','albums':archives}}
    (output/'gallery-import.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    if failures:(output/'skipped-files.json').write_text(json.dumps(failures,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'DONE: {len(photos)} photos, {len(archives)} ZIP parts, {len(failures)} skipped.')
    print('Upload source photos to the originals/ prefix with the same subfolders. Upload output thumbs/, views/ and archives/ to the storage bucket root. Import gallery-import.json in admin. Nothing was uploaded by this script.')
if __name__=='__main__':main()
