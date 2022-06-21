export function isUrlValid(url) {
  return url.includes(".") && url.length >= 3 && url[url.length - 1] != ".";
}
