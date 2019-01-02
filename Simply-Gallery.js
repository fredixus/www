class gallery{
    constructor(nameOfParentClass, nameOfSubClass, nameSubIdElements){
        this.nameOfParentClass = nameOfParentClass;
        this.nameOfSubClass = nameOfSubClass;
        this.nameSubIdElements = nameSubIdElements;
    }
    alertData(){
        alert(this.nameOfParentClass+" : "+this.nameOfSubClass+" : "+this.nameSubIdElements);
    }
    get getNOPC(){                                                              //NOPC - Name Of Parent Class
        return this.nameOfParentClass; 
    }
    get getNOSC(){                                                              //NOSC - Name Of Sub Class
        return this.nameOfSubClass; 
    }
    get getNSIE(){                                                              //NSIE - Name Sub Id Elements
        return this.nameSubIdElements; 
    }
    get getNSIEh(){                                                             //NSIE - Name Sub Id Elements Hash
        return "#"+this.nameSubIdElements+"-"; 
    }
    get getNOSCd(){                                                             //NOSCd - Name Of Sub Class DOT
        return "."+this.nameOfSubClass; 
    }
}

function setUpIdName(nameOfParentClass, prefixOfId){                            //nameOfParentClass - user gives a name of class for elements where new ID is needed. 
    var parentElements = document.querySelectorAll(nameOfParentClass);          //prefixOfId - user set the name of ID, function automaticaly add to this sufix "-i" (where i is integer > 0)
    for (var i = 0; i < parentElements.length; i++) parentElements[i].id = prefixOfId + '-' + i;
}
function setId(nameOfParentClass, prefixOfId){                                  //nameOfParentClass - user gives a name of class for elements where new ID is needed.                                                                            
    var parentElements = document.querySelectorAll(nameOfParentClass);          //prefixOfId - user set the name of ID, function automaticaly add to this sufix "-i" (where i is integer > 0)
    parentElements.id = prefixOfId;
}
         
function setUpClassForElements(where,what){
    $(where+" img").addClass(what);
}

function toClose(nameOfGalleryClass, nameOfPhotosId,numberOfPhotos){
    console.log("To close with:"+nameOfGalleryClass+":"+nameOfPhotosId+":"+numberOfPhotos); 
	$(nameOfGalleryClass).css('background-color','rgba(0, 0, 0, .0)');
    $(nameOfGalleryClass).css('width','auto');
  	$(nameOfGalleryClass).css('height','auto');
  	$(nameOfGalleryClass).css('position','');
  	$(nameOfGalleryClass).css('top','');
    $("#close").css('display','none');
	$('.active').removeClass("active"); 
           
    for(var i = 0;i<numberOfPhotos;i++){
        console.log(nameOfPhotosId+i+": :"+widthness); 
		$(nameOfPhotosId+i).css('width',widthness+'px');
		$(nameOfPhotosId+i).css('height','auto');
		$(nameOfPhotosId+i).css('position','');
		$(nameOfPhotosId+i).css('top','auto');                                    
		$(nameOfPhotosId+i).css('left','auto');                                     
		$(nameOfPhotosId+i).css('margin','10px');
		$(nameOfPhotosId+i).css('text-align','center');
	} 
    counter = 0;   
}
var value = 0; var counter = 0;                                             //indicate the value 
const GAL = new gallery(".gallery","photo","photo");                        //create the gallery object
setUpClassForElements(GAL.getNOPC,GAL.getNOSC);                             //create class with name: GAL.getNOSC for elements within class  GAL.getNOPC
var numItems = $(GAL.getNOSCd).length;
/*Cout how many images are in gallery -- objects have to contain name od sub-class (with dot)*/
var widthness = $("img").width();
/*Get the width from parametr every img - img should be the same*/
//-------------------------------------------Before loading---------------------
$(".gallery").append('<span id="close"> X</span>');
/* Add new HTML markup with id close. Tkis feature close the active gallery. */

window.addEventListener("keydown", function(event) {
	if(event.key == "Escape" && counter==1){
        console.log("CLose with Escape key"); 
		toClose(GAL.getNOPC,GAL.getNSIEh,numItems); 
	}
}, true);
/* Add new listener. Script listen if Esc is clicked gallegry is closed. */

//-------------------------------------------After loading----------------------
$(document).ready(function() {
	
	//alert(widthness);
    var deviceHeight = $(document).height();                                    //document or window
    var deviceWidht = $(document).width();                                      //document or window
    var wal = (deviceWidht/2) - ((deviceWidht*60)/100)/2;
	var wigthOfPhoto = 2/3*((deviceWidht - 50  - (50*numItems))/ numItems);
	var leftSpace = (deviceWidht - (numItems*wigthOfPhoto+250))*0.5;                     //set the left space for with of image (250) multipy over the number of items. This value is minused from page width, eferythink devided by 2. 
	
	
	console.log(wigthOfPhoto+":"+leftSpace);  
    $(GAL.getNOSCd).click(function() {
    var idName = $(this).attr('id');
    var setIdName = '#'+idName;
    console.log("idName + setIdName: "+setIdName+":"+idName);
    
	if($(this).attr('class') == GAL.getNOSC+" active"){
        console.log("Minimalize the photo: Display IF [$(this).attr('class')]:"+$(this).attr('class')+"=="+GAL.getNOSC+" active"); 
		$(setIdName).css('position','fixed');
		$(setIdName).css('bottom','50px');
		$(setIdName).css('top','auto');
		$(setIdName).css('margin','10px');
		$(setIdName).css('width',wigthOfPhoto+'px');
		$(setIdName).css('height','auto');
		$(setIdName).css('left',leftSpace+(wigthOfPhoto+50)*(idName[idName.length-1])+'px');	
		$(this).removeClass("active");
		counter = 0;	
	}else if(counter==1 && $(this).attr('class') != GAL.getNOSC+" active"){
		console.log("capture 1:"+counter+" Class:"+$(this).attr('class')); 

		$('.active').css('position','fixed');
		$('.active').css('bottom','50px');
		$('.active').css('top','auto');
		$('.active').css('margin','10px');	
		$('.active').css('width',wigthOfPhoto +'px');                           // bug potencial
		$('.active').css('height','auto');
		$('.active').css('left',+value+'px');	
		$('.active').removeClass("active");
        	
        counter = 0;

        $(setIdName).fadeOut('fast', function() {	
		  $(GAL.getNOPC).css('background-color','rgba(0, 0, 0, .7)');
          $(GAL.getNOPC).css('width',deviceWidht+'px');
		  $(GAL.getNOPC).css('height',deviceHeight+'px');
		  $(GAL.getNOPC).css('position','absolute');
		  $(GAL.getNOPC).css('top','0px');
		  $(setIdName).css('width','60%');
		  $(setIdName).css('height','600px');	
		  $(setIdName).css('position','relative');
		  $(setIdName).css('top','50px');                                         //50px from top
		  $(setIdName).css('left',wal+'px');                                      //center the image.
          $(setIdName).css('margin','0 auto');                                  //not nesessary?
		  $(setIdName).css('text-align','center');
			                  
		for(var i = 0;i<numItems;i++){
			if(setIdName==GAL.getNSIEh+i){
				$(GAL.getNSIEh+i).addClass("active");                           //add class active to active element
				value = leftSpace+(wigthOfPhoto+50)*i;
                counter=1;                                                      //set up counter to 1 to determinate state of element.
			}else{
				$(GAL.getNSIEh+i).css('position','fixed');                      //change not clicked elements
				$(GAL.getNSIEh+i).css('bottom','50px');
				$(GAL.getNSIEh+i).css('left',leftSpace+(wigthOfPhoto+50)*i+'px');	
			}
		} 
    	$(this).fadeIn('fast');
	   });
	}else{
	$(setIdName).fadeOut('fast', function() {	
		$(GAL.getNOPC).css('background-color','rgba(0, 0, 0, .7)');             //set the background of web-page for better foto exposure
        $(GAL.getNOPC).css('width',deviceWidht+'px');                                  //set the width of Gallery
		$(GAL.getNOPC).css('height',deviceHeight+'px');                             //set the height of Gallery
		$(GAL.getNOPC).css('position','absolute');                              //set the position of Gallery to absolute
		$(GAL.getNOPC).css('top','0px');                                        //set the top space from top to 0px
        $(setIdName).css('width','60%');                                        //set the width of choosen image
		$(setIdName).css('height','600px');       	                            //set the height of choosen image
		$(setIdName).css('position','relative');                                //set the position of choosen image to relative
		$(setIdName).css('top','50px');                                         //move image 50px from top
		$(setIdName).css('left',wal+'px');                                      //center the image  [($(document).width()/2) - (($(document).width()*60)/100)/2]
		//$(setIdName).css('margin','0 auto');
		//$(setIdName).css('text-align','center');			                  
		for(var i = 0;i<numItems;i++){
			if(setIdName==GAL.getNSIEh+i){
				$(GAL.getNSIEh+i).addClass("active");                           //add class active to active element
				value = leftSpace+(wigthOfPhoto+50)*i;
                counter=1;                                                      //set up counter to 1 to determinate state of element.
			}else{
				$(GAL.getNSIEh+i).css('position','fixed');                      //change not clicked elements
				$(GAL.getNSIEh+i).css('bottom','50px');
				$(GAL.getNSIEh+i).css('left',leftSpace+(wigthOfPhoto+50)*i+'px');
				$(GAL.getNSIEh+i).css('width',wigthOfPhoto+'px');	
			}
		} 
    	$(this).fadeIn('fast');
	});	
	}
    var testy = 0;
    if(testy == 0 ){
    	$("#close").css('display','block');  
    }else{
    	testy = 1;
    }  
    });
    /*Makes the close markup visible*/  
    $("#close").click(function() {
        console.log("CLose with #close tag"); 
		toClose(GAL.getNOPC,GAL.getNSIEh,numItems);    
    });  
    setUpIdName (GAL.getNOSCd, GAL.getNSIE);      
});