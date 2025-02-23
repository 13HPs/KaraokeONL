const socket = io('http://localhost:5000');

// Connection events
socket.on('connect', () => {
    console.log('Connected to server');
});

socket.on('connect_error', (error) => {
    console.error('Connection error:', error);
});

socket.on('disconnect', () => {
    console.log('Disconnected from server');
});
window.alert = function(message) {
    document.getElementById('customAlertContent').textContent = message;
    const alertModalElement = document.getElementById('customAlertModal');
    document.body.appendChild(alertModalElement);
    const alertModal = new bootstrap.Modal(alertModalElement, { backdrop: true });
    alertModal.show();
};
function deactivateModal(ModalId) {
    const modalElement = document.getElementById(ModalId);
    const modalInstance = bootstrap.Modal.getInstance(modalElement);
    modalInstance.hide();
    const backdrop = document.querySelector('.modal-backdrop');
    if (backdrop) {
        backdrop.remove();
    }
    document.body.classList.remove('modal-open');
}