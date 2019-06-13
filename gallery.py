import webbrowser

mydict={
    0:'lion.jpg',
    1:'elephant.jpg',
    2:'tiger.jpg',
    3:'zibra.jpg',
    4:'unicorn.jpg',
    5:'cat.jpg',
    6:'goat.jpg',
    7:'fox.jpg',
    8:'dog.jpg',
    9:'crocodile.jpg',
    10:'giraffe.jpg'
}

f = open('webpage.html','w')
html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="pstyle.css">
<link href="https://use.fontawesome.com/releases/v5.0.6/css/all.css" rel="stylesheet">
<link  href="http://fonts.googleapis.com/css?family=Anton"  rel="stylesheet" type="text/css">
<link  href="http://fonts.googleapis.com/css?family="Indie Flower""  rel="stylesheet" type="text/css">
</head>
<body>
"""
html+="""
<header class="Headclass">
    <div id="tb">
    <button type="submit"><i class="fa fa-home"></i></button>
    <button type="submit"><i class="fa fa-info"></i></button>
    <button type="submit"><i class="fa fa-clipboard"></i></button>
    </div>
    <h1>Africa</h1>
</header>
"""

html +="<ol>"
for n in range(11):
    html+=f"<div><img src={mydict[n]}"+"><br/>"
    html+="""
    <button type="submit">Info</button>
    """
    html+="</div>\n"
html +="</ol>"

html +="""
</body>
</html>"""
print(html)
f.write(html)
f.close()
webbrowser.open_new_tab('webpage.html')




c = open('pstyle.css','w')
css = """

body{
    width:100%;
    height:100%;
    background-color: rgb(0,70,0);
    margin:0;
    overflow-x: hidden;
}
h1{
    width:500px;
    height:auto;
    transform: translate(400px, 0px);
    font-family:Anton,Serif;
    font-size:100pt;
    text-align:center;
    margin:0;
    padding:0;
    color:#C0C0C0;
}
div{
    float:left;
    position:absloute;
    margin:10px;
}
ol{
    position:relative;
    list-style-type: none;
    margin:0;
}
img{
width:400px;
margin:0px;
height:200px;
}
button{
width:70px;
height:40px;
transform: translate(150px, 0px);
background-color:brown;
border-radius:5px;
cursor:pointer;
font-family:"Indie Flower",Serif;
}
#tb{
position:absolute;
transform: translate(950px, 20px);
margin:0;
padding:0;
}
.Headclass{
position: relative;
width:100%
height:auto;
margin:0;
padding:0;
background:linear-gradient(90deg,#FF0000,#00FF00,#0000FF);
background-size:100% 100%;
animation: gradient 5s infinite;
}
@keyframes gradient{
50% {background-position: 50% 0;}
}
header div button{
 background-color:yellow;
}
"""
print(css)
c.write(css)
c.close()
