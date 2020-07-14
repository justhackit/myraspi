import os
import time

html_prt1="""
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx from RaspberryPi!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx that is running on RaspberryPi!</h1>

<p id="date"></p>
<script>
document.getElementById("date").innerHTML = Date();
</script>

<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<pre><em>
"""
html_prt3="""
</em></pre>
</body>
</html>
"""

if __name__ == '__main__':
    html_part2=""
    for commd in ["date","vcgencmd measure_temp","iostat -c","free -m","df -h /","lsblk"]:
        for line in os.popen(commd):
            html_part2=html_part2+line

    html_code=html_prt1+html_part2+html_prt3
    print(html_code)
    with open("/var/www/html/index.nginx-debian.html", "w") as text_file:
        text_file.write(html_code)
    

