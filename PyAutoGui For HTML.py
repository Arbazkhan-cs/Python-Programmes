import pyautogui
import time
time.sleep(5)

# pyautogui.typewrite("<!DOCTYPE html>\n")
# pyautogui.typewrite("<html lang='en'>\n")
# pyautogui.typewrite("<head>\n")
# pyautogui.typewrite("<meta charset='UTF-8'>\n")
# pyautogui.typewrite("<meta http-equiv='X-UA-Compatible' content='IE=edge'>\n")
# pyautogui.typewrite("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
# pyautogui.typewrite("<meta name='discription' content='This Is My Web Site'>\n")
# pyautogui.typewrite("<link rel='stylesheet' href='Web_Demo.css'>\n")
# pyautogui.typewrite("<title>HOME</title>\n")
# pyautogui.typewrite("</head>\n")
# pyautogui.typewrite("<body>\n")
# pyautogui.typewrite("<header>\n")
# pyautogui.typewrite("<div class='div1'>\n")
# pyautogui.typewrite("<div class='ring'></div>\n"
#                     "<div class='ring'></div>\n"
#                     "<div class='ring'></div>\n")
# pyautogui.typewrite("</div> \n <nav class='navbar'> \n <ul id='ul1'> \n <li class='li'><a href='#' target='_self' class='a'>Home</a></li> \n <li><a href='#about' target='_self'>About</a></li> \n <li><a href='#services' target='_self'>Services</a></li> \n <li><a href='#contact' target='_self'>Contact Us</a></li> \n </ul> \n </nav> \n <nav class='login'> \n <ul> \n <li><a href='#' target='_blank'>Login</a></li> \n <li><a href='/websites/SignUp Form/signup.html' target='_blank'>Sign Up</a></li> \n </ul> \n </nav> \n \n </header> \n <div class='marquee'> \n <marquee>Welcome To My website</marquee> \n </div> \n <div class='imgdiv'> \n <img src='/images/Artificial-Intelligence.jpg' alt='tech_qutes' class='img' title='Artificial Inteligence'> \n </div> \n <div class='h2' id='about'> \n <H2 title='Modern Generation AI'>About</H2> \n </div> \n \n <div class='p'>\n<p>\nThe modern generation of the world is technologically advanced, and the pace of advancements and\nimprovements\nis continuously increasing with no signs of slowing down. The current era we all live in will prove to be\nthe most influential period of all time.\n</p>\n<p>\nThe Curve of improvements in humanity has always tended to be an exponential curve. With the discovery of\nthe fire way dating back to thousands of years ago, to the discovery of the wheel, to the inventions of\nhigh-quality developments in the 17th and 18th Century, and finally, to the modern era of technological\nadvancements where the majority of the inventions have been made.\n</p>\n<p>\nThe inventions and discoveries in the past two to three decades have almost been double that of the overall\nproducts in all the previous years combined. With the human intellect improving each day, and with the rise\nof Artificial Intelligence and Data Science of the Horizon, the modern technologies of AI will impact the\nworld like never before and change the landscape of the entire future.\n</p>\n<p>\nThe concepts of artificial intelligence, machine learning, and neural networks have existed for almost over\na century now. However, despite their brief initial success, they never had the time to shine. The main\nreasons for their failure were due to the fact that the advancements in technology had not yet reached their\nfull potential. And also, there was not enough data available for deep learning models and neural networks\nto create a significant impact.\n</p>\n<p>\nThe popularity of deep learning blew up as recently as only about a decade ago. The reemergence of the hype\nof neural networks resulted from an incident in 2012 where a team led by George E. Dahl won the “Merck\nMolecular Activity Challenge” using multi-task deep neural networks to predict the biomolecular target of\none drug. After this incident, deep learning and neural networks have been used continuously in performing\nvarious tasks related to image segmentation, object detection, and so much more.\n</p>\n<p>\nI would highly recommend checking out the following article on the complete interesting and convoluted\nhistory of neural networks from the link provided below. It provides a detailed and concise guide on the\nhistorical events that have now led to the popularity of deep learning and neural networks.\n</p>\n</div>\n<div class='services' id='services'>\n<h2>Services Of AI</h2>\n</div>\n<div class='p_services'>\n<div id='ml' class='service'>\n<span>\nMachine Learning:\n</span>\n<p>\nMachine learning is an application of artificial intelligence (AI) that provides systems the ability to\nautomatically learn and improve from experience without being explicitly programmed. Machine learning\nfocuses on the development of computer programs that can access data and use it to learn for themselves.\n</p>\n</div>\n<div id='cv' class='service'>\n<span>\nComputer Vision:\n</span>\n<p>\nComputer vision is a field of artificial intelligence (AI) that enables computers and systems to derive\nmeaningful information from digital images, videos and other visual inputs — and take actions or make\nrecommendations based on that information. If AI enables computers to think, computer vision enables\nthem to see, observe and understand.\n</p>\n</div>\n</div>\n<footer id='contact'>\n<div class='contactus'>\nContact Us\n</div>\n<div class='contact'>\nEmail:\n<a href='mailto:arbazkhan.msit@gmail.com' target='_blank'>\n<img src='/images/Gmail-Logo.png' alt='arbazkhan.msit@gmail.com'>\n</a>\n</div>\n<div class='contact'>\nFacebook:\n<a href='https://www.facebook.com/profile.php?id=100009194652794' target='_blank'>\n<img src='/images/facebook-logo.png' alt='Arbaz khan'>\n</a>\n</div>\n<div class='contact'>\nInstagram:\n<a href='https://www.instagram.com/khangamer_yt_ff/' target='_blank'>\n<img src='/images/Instagram_logo.png' alt='khangamer_yt_ff'>/\n</a>\n</div>\n</footer>\n</body>\n</html>")

pyautogui.typewrite("""
*{
    margin: 0;
    padding: 0;
}
body{
    background-color: #fffcf4;
    /* background: url("/images/box.png"); */
    background-attachment: fixed;
}
/* ------------------------------------------------Navigation Bar-------------------------------------------------------------- */
/* ---------------------------------------------------------------------------------------------------------------------------- */
header{
    background-color: #021239;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 1;
    position: sticky;
    top:0px;
}


/* --------------Navigation Image--------------------- */
.nav-img{
    position: relative;
    top: 5vh;
    left:6vw;
    width: 5vw;
    border-radius: 15px;
    z-index: 1;
}


/* --------------Navigation Mainue------------------- */
.main-nav ul{
    position: relative;
    display: flex; 
    list-style: none;  
    gap: 5vw; 
}
.main-nav ul li a{
    text-decoration: none;
    font-size: 1.5vw;
    color: white;
    transition: 0.6s;
}
.main-nav ul li a:hover{
    color: orangered;
}
.main-nav ul li a:focus{
    color: orangered;
}


/* -------------Navigation Search Engine----------------- */
.nav-search{
    position: relative;
    display: flex;
    align-items: center;
    right: 30px;
    gap: 5px;
}
#search{
    width: 10vw;
    height: 3vh;
}




/* ---------------------------------------------------Main Container-------------------------------------------------------- */
/* ------------------------------------------------------------------------------------------------------------------------ */

/* -------------------------------------------------Qute Image------------------------------------------------------------- */
.img-container{
    position: relative;
    background-image: url("/images/banner-bg.png");
    background-size: 2000px;
    height: 90vh;
    background-repeat: no-repeat;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
}

.img-container q{
    position: absolute;
    font-size: 5vw;
    width: 70%;
    left: 20vw;
    top: 10vh;
    word-spacing: 20px;
    color: white;
}

/* --------------------------------------------------------About---------------------------------------------------------- */
.about-container{
    display: flex;
    justify-content: space-between;
    margin: 100px 80px;
}


/* ---------------------------------about text---------------------- */
.about{
    width: 40vw;
}
.about h1{
    font-size: 5vw;
}
.about p{
    font-size: 2vw;
    font-family: 'Cormorant Garamond', sans-serif;
}


/* -----------------------------------about image------------------------------ */
.about-img{
    display: flex;
    background-color: #E2E2E2;
    border-radius: 100px;
    align-items: center;
}
.about-img-{
    width: 30vw;
}


/* ----------------------------------More Button------------------------------------- */
.more a{
    font-size: 2vw;
    padding: 0.6vh 5vw;
    margin-top: 30px;
    background-color: orangered;
    border-radius: 10px;
    color: white;
    text-decoration: none;
    transition: 0.5s;
    
}

.more{
    margin-top: 30px;
}

.more a:hover{
    background-color: black;
}


/* ---------------------------------------------------------Services------------------------------------------------------ */

.service{
    text-align: center;
    font-size: 3vw;
}


/* -----------------------Services Images----------------------- */
.service-img ul{
    display: flex;
    list-style: none;
    justify-content: space-evenly;
    align-items: center;
}

.service-img ul li img{
    width: 20vw;
    border-radius: 10px;
}

.s-img:hover{
    width: 24vw;
}


/* ----------------------Services Images Haidings-------------------- */
#li1{
    position: relative;
    left:-3vw;
    font-size: 1vw;
}
#li2{
    position: relative;
    left:-1vw;
    font-size: 1vw;
}
#li3{
    position: relative;
    left:-0.5vw;
    font-size: 1vw;
}
#li4{
    font-size: 1vw;
}


/* -----------------------------------More--------------------- */
.service-more{
    margin-left: 4vw;
}


/* =========================================================Footer=========================================================== */
.footer{
    margin-top: 10vh;
    background-color: #021239;
    padding: 2vw;
}
.footer{
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.footer div a{
    display: flex;
    justify-content: space-between;
    align-items: center;
    text-decoration: none;
    color: white;
    font-size: 2vw;;
    transition: 0.5s;
}

.footer div a:hover{
    color: orangered;
}


.footer div img{
    width: 3vw;
}

footer{
    background-color: #d2bd2d;
    color:white;
    text-align: center;
}

""")
