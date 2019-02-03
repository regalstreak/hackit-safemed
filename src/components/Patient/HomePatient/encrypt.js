import crypto from 'crypto';

export const encrypt = (buffer, password, iv) => {
    var cipher = crypto.createCipheriv('aes-256-ctr', password, iv);
    var crypted = Buffer.concat([cipher.update(buffer), cipher.final()]);
    return crypted;
}

export const decrypt = (buffer, password, iv) => {
    var decipher = crypto.createDecipheriv('aes-256-ctr', password, iv);
    var dec = Buffer.concat([decipher.update(buffer), decipher.final()]);
    return dec;
}