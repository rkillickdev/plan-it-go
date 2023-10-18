// Replace Text In Header using the ReplaceMe.js v1.1.0 script
// The idea for this came from the following Udemy Bootstrap Tutorial:
// https://www.udemy.com/course/bootstrap-from-scratch/learn/lecture/38477274#search

const checkReplace = document.querySelector('.replace-me')

if (checkReplace !== null) {
  const replace = new ReplaceMe(checkReplace, {
    animation: 'animated fadeIn',
    speed: 4000,
    separator: ',',
    loopCount: 1,
    autoRun: true,
  });
}