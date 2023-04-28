const signinDialog = document.getElementById('signin-dialog');
const signupDialog = document.getElementById('signup-dialog');
const rideLinkDialog = document.getElementById('ride-link-dialog');
const signinBtn = document.getElementById('signin-btn');
const signupBtn = document.getElementById('signup-btn');
const rideLinkBtn = document.getElementById('join-link');

function openSigninDialog() {
    signinDialog.showModal();
}

function openSignupDialog() {
    signupDialog.showModal();
}

function openLinkDialog() {
    rideLinkDialog.showModal();
}

function closeSigninDialog() {
    signinDialog.close();
}

function closeSignupDialog() {
    signupDialog.close();
}

function closeLinkDialog() {
    rideLinkDialog.close();
}

signinBtn.addEventListener('click', openSigninDialog);
signupBtn.addEventListener('click', openSignupDialog);
rideLinkBtn.addEventListener('click', openLinkDialog);