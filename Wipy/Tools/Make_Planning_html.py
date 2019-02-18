
with open('planning.html','a') as f:
    for _ in range(20):
        f.write("""
<div>
{0:02}
<input type="number" name="h{0}" value="0" min="0" max="23">
<input type="number" name="m{0}" value="0" min="0" max="59">
<input type="checkbox" id="v{0}" name="c{0}"/>
<SELECT name="p{0}" size="1">
<OPTION>1
<OPTION>2
<OPTION>3
<OPTION>4
<OPTION>5
<OPTION>6
<OPTION>7
<OPTION>8
<OPTION>9
<OPTION>Standard
<OPTION>Pailleux
<OPTION>DVT
<OPTION>MultiTas
</SELECT>
</div>
""".format(_+1))



T3PlanRequest = b'POST /T3Plan HTTP/1.1\r\nHost: 192.168.4.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://192.168.4.1/Plan\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 345\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\nh1=4&m1=0&p1=1&h2=0&m2=0&c2=on&p2=1&h3=0&m3=5&p3=Standard&h4=0&m4=0&p4=1&h5=0&m5=0&p5=1&h6=0&m6=0&p6=1&h7=0&m7=0&p7=1&h8=0&m8=0&p8=1&h9=0&m9=0&p9=1&h10=0&m10=0&p10=1&h11=0&m11=0&p11=1&h12=0&m12=0&p12=1&h13=0&m13=0&p13=1&h14=0&m14=0&p14=1&h15=0&m15=0&p15=1&h16=0&m16=0&p16=1&h17=0&m17=0&p17=1&h18=0&m18=0&p18=1&h19=0&m19=0&p19=1&h20=0&m20=0&p20=1' 


Web Request=b'GET /Plan HTTP/1.1\r\nHost: 192.168.4.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nCache-Control: max-age=0\r\n\r\n'
