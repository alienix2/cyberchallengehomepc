/* String.prototype.obf = function () {
    var bytes = [];
    for (var i = 0; i < this.length; i++) {
        bytes.push(this.charCodeAt(i).toString(16));
    }
    return bytes.join('$');
} */

/* String.prototype.deobf = function () {
    var arr = this.split('$');
    return arr.map(function(c) { 
        return String.fromCharCode(parseInt(c, 16))
    }).reduce(function(a, b) {return a  + b})
} */

var api_user = "apiadmin";
var api_password = "43$43$49$54$7b$38$30$30$62$30$63$32$31$2d$33$34$37$36$2d$34$33$62$34$2d$62$65$64$31$2d$30$30$61$35$39$34$36$65$30$34$64$35$7d"
