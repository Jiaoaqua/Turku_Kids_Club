// main.js

document.addEventListener('DOMContentLoaded', function () {
  const likeButtons = document.querySelectorAll('.like-btn');
  likeButtons.forEach(button => {
    button.addEventListener('click', function () {
      const clubName = button.getAttribute('data-club-name');

      // 发送 AJAX 请求到后端视图
      fetch(`/like-club/${clubName}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ liked: !button.classList.contains('liked') })
      })
        .then(response => response.json())
        .then(data => {
          if (data.success) {

            if (button.classList.contains('liked')) {
              button.textContent = 'Like ❤';
              button.classList.remove('liked');
            } else {
              button.textContent = 'Unlike 🖤';
              button.classList.add('liked');
            }
            alert(data.message);
          } else {

            alert(data.error);
          }
        })
        .catch(error => {
          console.error('Error:', error);
        });
    });
  });
});


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function openReviewModal(clubName) {
  console.log("clubName:", clubName);
  var modal = document.getElementById("reviewModal");
  var textarea = document.getElementById("reviewTextarea");
  var clubNameInput = document.getElementById("clubNameInput");  // 获取隐藏字段

  textarea.value = "";
  clubNameInput.value = clubName;  // 设置隐藏字段的值为当前俱乐部名字

  modal.style.display = "block";
}

window.onload = function () {
  document.getElementById("submitReviewBtn").addEventListener("click", submitReview);
};
function submitReview() {
  var clubName = document.getElementById("clubNameInput").value;
  var reviewContent = document.getElementById("reviewTextarea").value;
  var url = "/submit_review/" + encodeURIComponent(clubName) + "/";

  var data = {
    clubName: clubName,
    content: reviewContent
  };

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie("csrftoken")
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        alert("Woohoo! Your review has been posted successfully!");
      } else {
        alert("Oops! We couldn't post your review. Try again?" + data.error);
      }
    })
    .catch(error => {
      console.error('Error:', error);
      alert("Failed");
    });
}


function closeReviewModal() {
  var modal = document.getElementById("reviewModal");
  modal.style.display = "none";
}