document.getElementById('update-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;

    fetch('/update_profile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: username })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById('name').textContent = data.name;
            document.getElementById('email').textContent = data.email;
            document.getElementById('login').textContent = data.login;
            document.getElementById('location').textContent = data.location;
            document.getElementById('bio').textContent = data.bio;
            document.getElementById('stars').textContent = data.stars;
            document.getElementById('commits').textContent = data.commits;
            document.getElementById('repos').textContent = data.repos;
            document.getElementById('followers').textContent = data.followers;
            document.getElementById('following').textContent = data.following;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});