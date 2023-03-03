$(document).ready(function(){ 
    var template = $('#test').html();
    var output = $('#output');
  
    var data = {
        "Subject": "Template Engines",
        "names": [
            {"name": "Mustache"},
            {"name": "HandleBar"}
        ]
    };
  
    var result = Mustache.render(template, data);
    
    output.append(result);
  
  });