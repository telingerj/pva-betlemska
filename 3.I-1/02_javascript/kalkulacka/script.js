function load()
{
    let btn = document.getElementById("ok");
    btn.onclick = compute;
    let btn2 = document.getElementById("ok2");
    btn2.onclick = prime;
}

function compute()
{
    let num1 = document.getElementById("num1");
    let num2 = document.getElementById("num2");
    let operation = document.getElementById("operation");
    if (operation.value == "+")
    {
        alert(parseInt(num1.value) + parseInt(num2.value));
    }
    else if (operation.value == "-")
    {
        alert(parseInt(num1.value) - parseInt(num2.value));
    }
    else if (operation.value == "*")
    {
        alert(parseInt(num1.value) * parseInt(num2.value));
    }
    else if (operation.value == "/")
    {
        alert(parseInt(num1.value) / parseInt(num2.value));
    }
    else
    {
        alert("tuhle operaci neznám");
    }
}

function prime()
{
    let num3 = document.getElementById("num3");
    let n = parseInt(num3.value);
    let isPrime = true;
    for (let i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            isPrime = false;
            break;
        }
    }
    if (isPrime)
    {
        alert("je to prvočíslo");
    }
    else
    {
        alert("není to prvočíslo");
    }
}

window.onload = load;