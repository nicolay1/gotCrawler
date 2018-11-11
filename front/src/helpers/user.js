import Jwt from './jwt'

export default class User{
    constructor(){
        this.__user = (new Jwt()).user;
    }

    get id(){
        return this.__user.id
    }
    get firstname(){
        return this.__user.firstname
    }
    get surname(){
        return this.__user.surname
    }
    get poster(){
        return this.__user.poster
    }

    connected(){
        return this.__user !== null
    }

    static disconnect(){
        window.localStorage.removeItem('jwtToken')
    }
}