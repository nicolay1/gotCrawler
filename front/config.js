class config{
    constructor(){
        this.__backUrl = "http://localhost:5000/"
    }
    get backUrl(){
        return this.__backUrl
    }
}

export default (new config())
