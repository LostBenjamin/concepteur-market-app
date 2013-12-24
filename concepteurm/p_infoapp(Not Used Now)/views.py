# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("""<!DOCTYPE html>
<html>
<head>
<title>Profile</title> 
<meta lang="en">
<meta content="html/text; charset=UTF-8" >
<script type="text/javascript" src=""></script>
<script src="http://d3lp1msu2r81bx.cloudfront.net/kjs/js/lib/kinetic-v4.6.0.min.js"> </script>
<style>
 html {
    background-color: white;
 padding: 25px;
} 

#banner {
	position: fixed;
	background: none repeat scroll 0% 0% black;
	width: 100%;
	left: 0px;
    top: 0px;
    height: 80px;
	display: inline-block;
 }


#logoImage {
	float: left;
	position: relative;
	left: 0px;
	top: 0px;
}


 

.top_menu ul ul {
    display: none;
}

    .top_menu ul li:hover > ul {
        display: block;
    }


.menu {
    border:1px solid #ccc;
    border-width:1px 0;
    list-style:none;
    margin:0;
    padding:0;
    text-align:center;
}

.menu li{
    display:inline;
bottom: 50px;
}
.menu a{
    display:inline-block;
    padding:10px;




}
  


</style>

</head>

<!-- This is the document for the structure for the profile page main! 
This is structured in HTML/HTML5 and will use CSS/CSS3, and is based on the UI/UX of the .PSD & PDF files.
CSS naming structure throughout the site will be consistent in regards to the particular area serviced -->
<body>
    <header>
        <div id="logoImage"><img src="/logo_03.png"></img></div>
        <span id="banner"></span>
        <!-- <li><a href="#"><img src="x-icon of user"></img>USER NAME</a> 
        <nav class="top_menu">
            <ul>  < drop down-menu to be built using CSS/CSS3 or javascript. *preferred method CSS3 
                <li><a href="">PROFILE</a></li>
                <li><a href="">SETTINGS</a></li>
                <li><a href="">PERSONAL INFORMATION</a></li>
                <li><a href="">SAVED LOOKS</a></li>
                <li><a href="">MESSAGES</a></li>
                <li><a href="">FRIENDS</a></li>
                <li><a href="">FIND PEOPLE</a></li>
                <li><a href="">REWARDS</a></li>
                <li><a href="">EDIT AVATAR</a></li>
                <li><a href="">CONTACT US</a></li>
            </ul>
        </nav>
        </li> -->
        <nav class="menu">
            <ul>
                <li><a href="profile.html">PROFILE</a></li>
                <li><a href="settings.html">SETTINGS</a></li>
                <li><a href="personalinfo.html">PERSONAL INFO</a></li>
                <li><a href="savedlooks.html">SAVED LOOKS</a></li>
                <li><a href="messages.html">MESSAGES</a></li>
                <li><a href="friends.html">FRIENDS</a></li>
                <li><a href="findpeople.html">FIND PEOPLE</a></li>
                <li><a href="rewards.html">REWARDS</a></li>
                <button><a href="shopnow.html">SHOP NOW</a></button>
            </ul>
        </nav>
    </header> 

   <div>
       <!--This div contains the profile picture information for the user -->
       <img src="#from the backend somewhere...(user)"></img>
       <p>User name</p>
       <a href="personal information"><span>Change Photo</span></a> <!-- span is for design aesthetic base on UI/UX -->
   </div>

<!--     Flash area for 3D model to be placed in the middle: (please consult Naomi) for help with this area -->






<!-- Flash area .................................... 3D model.......END................................-->

   <div>
       <a href="back to create avatar area"><span>EDIT AVATAR</span></a>
       <a href="Upload look to feed from saved look private area"><span>UPLOAD TO THE FEED</span></a>
       <span class/id="for rotating button"></span> <!-- This will be inherited throughout the website with by CSS)-->
   </div>



<!--      Moodboard/Looksfeed Area Start: (Looks feed consult Naomi in regards to looksfeed
                                                   and Yuan for MoodBoard for help)     
 Will require Javascript/Jquery to switch out of the different areas between Looksfeed & MoodBoard -->
    
    <!--MoodBoard start-->
    <button class/id="" type="button">Open Feed</button>
    <p><span>MOODBOARD</span></p>
    <button type="button" class/id="">Create New</button>
    

    <!-- inside moodboard functionaity: Please refine Wendy, and base it on the UI/UX design
        <div class/id="for moodboard">
        <div class/id=""  ondrop="drop(event)" ondragover="allowDrop(event)"></div>
        <div class/id="">
          <button class/id="">
            Save Moodboard
          </button>
        </div>
    

        <div id="image_menu">
        <table id="item_table" border="1px">
            <tr id="dress">
                <td><img id="dress_1" src = "images/dress_1.jpeg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="dress_2" src = "images/dress_2.jpg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="dress_3" src ="images/dress_3.jpg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="dress_4" src ="images/dress_4.jpg" draggable="true" ondragstart="drag(event)" /></td>
            </tr>
            <tr id="handbag">
                <td><img id="handbag_1" src = "images/handbag_1.jpeg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="handbag_2" src = "images/handbag_2.jpg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="handbag_3" src ="images/handbag_3.jpg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="handbag_4" src ="images/handbag_4.jpg" draggable="true" ondragstart="drag(event)" /></td>
            </tr>
            <tr id="accessory">
                <td><img id="accessory_1" src = "images/accessory_1.jpg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="accessory_2" src = "images/accessory_2.jpg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="accessory_3" src ="images/accessory_3.jpg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="accessory_4" src ="images/accessory_4.jpg" draggable="true" ondragstart="drag(event)" /></td>
            </tr>
            <tr id="shoe">
                <td><img id="shoe_1" src = "images/shoe_1.jpg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="shoe_2" src = "images/shoe_2.jpg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="shoe_3" src ="images/shoe_3.jpg" draggable="true" ondragstart="drag(event)" /></td>
                <td><img id="shoe_4" src ="images/shoe_4.jpg" draggable="true" ondragstart="drag(event)" /></td>
            </tr>
        </table>
    </div> 
  </div>
  <div id="displayMoodBoard"></div>
    
                    Mooodboard End-->


<!--Looks Feed Start -->

   <p><span>LOOKS FEED</span></p>
   <button type="button" class/id="">OPEN MOODBOARD</button> 

<!-- Looks Feed End -->


    <footer class="for footer">
        <nav>
    	<h1>COMPANY INFORMTION</h1>
    	    <ul>
    	    	<li><a href="aboutus.html">ABOUT US</a></li>
    	    	<li><a href="features.html">FEATURES</a></li>
    	    	<li><a href="privacypolicy.html">PRIVACY POLICY</a></li>
    	    	<li><a href="tos.html">TERMS OF SERVICE</a></li>
            </ul>
        <h1>OUR DESIGNERS</h1>
            <ul>
            	<li><a href="designersatoz.html">A-Z</a></li>
            	<li><a href="designersignup.html">DESIGNER SIGN UP</a></li>
            </ul>
        <h1>CUSTOMER SERVICE</h1>
            <ul>
            	<li><a href="customerservice.html">CUSTOMER SERVICE</a></li>
            </ul>
        <h1>FOLLOW US</h1>
            <ul>
            	<li><a href="facebook">Facebook</a></li>
            	<li><a href="twitter">Twitter</a></li>
            	<li><a href="pinterest">Pinterest</a></li>
            </ul>
        </nav>
    </footer>




</body>
</html> 
""")

