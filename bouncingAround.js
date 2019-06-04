int r = 30;
int xpos;
int ypos;
int xspeed= 3;
int yspeed= 3;

void setup(){
size(600,400);
int r = 30;
int xpos;
int ypos;
int xspeed= 3;
int yspeed= 3;
xpos= 30;
ypos= 30;
}

//infinite loop
void draw(){
background(0,0);
xpos= xpos + xspeed ;
ypos= ypos + yspeed;
bounce();
ellipseMode(RADIUS);
ellipse(xpos,ypos,30,30);
}



void bounce(){
if (xpos > 600-r){
  xspeed*= -1;
  fill(255, 0, 0);
}

if (xpos < r){
  xspeed*= -1;
  fill(255,255,0);
}

if (ypos > 400-r){
  yspeed*= -1;
  fill(0,128,0);
}

if (ypos < r){
  yspeed= yspeed*-1;
  fill(0,0,255);
}
}