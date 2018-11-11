export default class Jwt{
    constructor(){
        this.__jwtToken = localStorage.getItem('jwtToken');
        this.__parsedToken = this.__extractJwtToken()
    }

    __extractJwtToken(){
        if(this.__jwtToken != null){
            try {
                return JSON.parse(atob(this.__jwtToken.split('.')[1]));
            } catch (e) {
                return null;
            }
        }
        return null;
    }

    get timeToExp(){
        return this.exp - Date().getTime();
    }
    get exp(){
        if(this.__parsedToken)
            return this.__parsedToken.exp;
        console.warn("Jwt exp attribute was called but no jwtToken detected.");
        return null
    }
    get user(){
        if(this.__parsedToken)
            return this.__parsedToken.user;
        return null
    }

    bearerToken(){
        return this.__jwtToken ? `Bearer ${this.jwtToken}` : ""
    }

    exist(){
        this.__jwtToken = localStorage.getItem('jwtToken');
        return this.__jwtToken !== null;
    }
    setToken(jwtToken){
        this.__jwtToken = jwtToken
        localStorage.setItem('jwtToken', jwtToken)
    }
}