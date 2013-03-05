function sayHello()
{
    name = document.getElementsByName("my")[0].value;//remove quotes
   if ((name=='no idea')|| (name == ""))
   {
       name = getDefaultName();
   }
   wishes = getWishes('morning')
   wishMe(wishes,name);
   //alert(name);
}

function getDefaultName()
{
   return "JAMES"
}

function getWishes(time)
{
    var name = "james";
   if (time =='morning')
   {
       wish = "Good Morning";
   }
   else if(time == 'afternoon')
   {
       wish = "Good Afternoon";
   }
   return wish;
}

function wishMe(sWishes,sName)
{
   alert(sWishes+' '+sName);
}


function addOne(a)
{
   var b = a + 1;
}
