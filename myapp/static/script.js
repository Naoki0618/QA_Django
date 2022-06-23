$(function () {
  // 検索項目のアコーディオン
  $('.contents_list').click(function () {
    var $answer = $('.answer');
    if ($answer.hasClass('open')) {
      $answer.removeClass('open');
      // slideUpメソッドを用いて、$answerを隠してください
      $answer.slideUp();

    } else {
      $answer.addClass('open');
      // slideDownメソッドを用いて、$answerを表示してください
      $answer.slideDown();

    }
  });
  $(".main_history").on("click",function(){
    $(this).next().slideToggle();
  });
});
