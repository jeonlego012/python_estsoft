from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64

# Create your views here.
def index(request):
    plt.plot(range(10))
    fig = plt.gcf() # get current figure
    
    # format: png
    buf = io.BytesIO() # byte buffer
    fig.savefig(buf, format='png') # 파일 말고 메모리(buf)에 저장
    buf.seek(0)
    string = base64.b64encode(buf.read()) # png값
    uri_png = urllib.parse.quote(string)
    
    # format: pdf
    buf.seek(0)
    fig.savefig(buf, format='pdf')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri_pdf = urllib.parse.quote(string)

    context = {
        'uri_png': uri_png,
        'uri_pdf': uri_pdf,
    }
    
    return render(request, 'main/index.html', context)