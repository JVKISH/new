
from rembg import remove 
from PIL import Image 


input_path = 'E:\C programs\ 
			Remove BackGround\gfgimage.png' 


output_path = 'E:\C programs\ 
			Remove BackGround\gfgoutput.png' 

input = Image.open(input_path) 

output = remove(input) 

output.save(output_path) 
