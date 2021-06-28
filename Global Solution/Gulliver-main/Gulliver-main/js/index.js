function slide1(){
    document.getElementById('id_slide').src="https://cdn.discordapp.com/attachments/820060898210873348/852920531224756244/guilherme-stecanella-SaVlzqe9068-unsplash_avpaulista.jpg";
    setTimeout("slide2()", 4000)
    }
    
    function slide2(){
    document.getElementById('id_slide').src="https://cdn.discordapp.com/attachments/828997750757654578/852939952270606376/joao-tzanno-jv_84by5ARA-banespa.jpg";
    setTimeout("slide3()", 4000)
    }
    
    function slide3(){
    document.getElementById('id_slide').src="https://cdn.discordapp.com/attachments/828997750757654578/852939402086973450/Ed_Martinelli.jpg";
    setTimeout("slide1()", 4000)
    }
