

def handle_uploaded_file(f, fname):
    ext = fname.split(".")[-1]
    with open('static\media\ + fname, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
