const signinDialog = document.getElementById('signin-dialog');
const signupDialog = document.getElementById('signup-dialog');
const rideLinkDialog = document.getElementById('ride-link-dialog');
const createRideDialog = document.getElementById('create-ride-dialog');
const signinBtn = document.getElementById('signin-btn');
const signupBtn = document.getElementById('signup-btn');
const rideLinkBtn = document.getElementById('join-link');
const createRideBtn = document.getElementById('create-ride');

function openSigninDialog() {
    event.preventDefault();
    signinDialog.showModal();
}

function openSignupDialog() {
    event.preventDefault();
    signupDialog.showModal();
}

function openLinkDialog() {
    rideLinkDialog.showModal();
}

function openCreateRideDialog() {
    createRideDialog.showModal();
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

function closeCreateRideDialog() {
    createRideDialog.close();
}

signinBtn.addEventListener('click', openSigninDialog);
signupBtn.addEventListener('click', openSignupDialog);
rideLinkBtn.addEventListener('click', openLinkDialog);
createRideBtn.addEventListener('click', openCreateRideDialog);