/*This variable returns a Boolean value depending on
if the browser is set to Dark Mode or Light Mode.
*/
const isDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

// This variable references the Favicon in layout.html.
const favicon = document.getElementById('favicon');

// The following logic changes the favicon if isDarkMode returns True
if (isDarkMode) {
  favicon.href = '/static/images/gamer-icon-dark.png';
}
