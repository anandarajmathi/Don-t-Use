function startDebugging()
{
    var welcome_slot = document.getElementById('welcome');
    welcome_slot.style.display = 'block';
}

function pauseOnBreakpoint()
{
    var oFrm = document.forms['using_firebug'];
    var who = oFrm['who'].value;
    var oFine = oFrm['hru'];
    for(i=0;i<oFine.length;i++)
    {
        if(oFine[i].checked)
        {
            alert(who+' is '+oFine[i].value)            
        }
    }
    var x = steppingInAndOut();
    var y = x-1;
    
}

function steppingInAndOut()
{
    var a = 1;
    for(i=0;i<10;i++)
    {
        a += 1;
    }
    return a;
}




