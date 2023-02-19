
function displayForm(formType){
    const form = document.getElementById(formType);

    console.log(form)
}

function clearAll(){
    const forms = ['locationform', 'budgetform'];
    for (let i=0; i<2; i++) {
        const form = document.getElementById(forms[i]);
        form.style.display = "none";
    }
}

function main(){
    document.addEventListener("click", function(evt) {
        console.log(evt.target.id);

        if (evt.target.id==='locationimg'){
            const form = document.getElementById("locationform");
            console.log(form.style);

            clearAll();

            form.style.display = "block";

            /*
            if (form.style.display ==="block") {
                form.style.display = "none";
                console.log('here')
            }
            else{
                form.style.display = "block";
                console.log('fail')
            }
            */
            
        }

        else if (evt.target.id==='budgetimg'){
            const form = document.getElementById("budgetform");
            console.log(form.style);
            console.log('bruh')
            /*

            if (form.style.display ==="block") {
                form.style.display = "none";
                console.log('here')
            }
            else{
                form.style.display = "block";
                console.log('fail')
            }
            */
            clearAll();

            form.style.display = "block";
        }

    });
    //displayDropdown(formType);
}

document.addEventListener('DOMContentLoaded', main);