/* Tools for manipulating strings */

/* Captialize first letter of string */
export function capitalize(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

/* Capitalize first letter and replace underscores with spaces */
export function splitCapitalize(string) {
  string = capitalize(string);
  return string.replace(/_/g, " ");
}
