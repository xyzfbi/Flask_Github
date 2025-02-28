function updateResume() {
    const resumeData = {
        name: document.getElementById('name-input').value,
        job_position: document.getElementById('job_position-input').value,
        work_place: document.getElementById('work_place-input').value,
        skills: document.getElementById('skills-input').value,
        experience: document.getElementById('experience-input').value,
        education: document.getElementById('education-input').value
    };

    fetch('/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(resumeData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('name').innerText = resumeData.name;
            document.getElementById('job_position').innerText = resumeData.job_position;
            document.getElementById('work_place').innerText = resumeData.work_place;
            document.getElementById('skills').innerText = resumeData.skills;
            document.getElementById('experience').innerText = resumeData.experience;
            document.getElementById('education').innerText = resumeData.education;
        }
    });
}