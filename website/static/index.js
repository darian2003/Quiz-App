function deleteQuiz(quizId) {
    fetch("/delete-quiz", {
      method: "POST",
      body: JSON.stringify({ quizId: quizId }),
    }).then((_res) => {
      window.location.href = "/dashboard"; // redirect to the dashboard page
    });
}
