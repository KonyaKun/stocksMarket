class registerView {
    #main = document.querySelector(".main");
    userForm;

    render(){
        const markup = this.#generateMarkup();
        this.#clearMain();
        this.#main.insertAdjacentHTML('afterbegin', markup);
        this.userForm = document.forms.registration;
    }

    #clearMain() {
        this.#main.innerHTML = '';
    }


    #generateMarkup() {
        return `
        <form 
            action="#" 
            method="post" 
            id="registration" 
            name="registration"
            class="form"
        >   
            <h1 class="sign">Регистрация</h1>
            <input class="inregistr" type="text" id="user_name" name="user_name" placeholder="Username" autocomplete="on">
            <input class="inregistr" type="text" id="first_name" name="first_name" placeholder="Firstname" autocomplete="on">
            <input class="inregistr" type="text" id="last_name" name="last_name" placeholder="Lastname" autocomplete="on">
            <input class="inregistr" type="email" id="email" name="email" placeholder="Email" autocomplete="on">
            <input class="inregistr" type="file" name="image_url" id="image_url">
            <input class="inregistr" type="password" name="password" id="password" placeholder="Password" autocomplete="on">
            <input class="inregistr" type="submit" value="Sign Up" class="submit">
        </form>

        <div class="loading_screen">
            <div class="load"></div>
        </div>
        `
    }
}

export default new registerView();