export function isUrlValid(url: string): boolean {
  return url.includes(".") && url.length >= 3 && url[url.length - 1] != ".";
}

export function timeTo(time: string): number {
  let num = "";
  let i = 0;
  const len = time.length;

  let year = 2023;
  while (time[i] >= "0" && time[i] <= "9" && i < len) num += time[i++];
  if (num.length >= 4) year = Number(num.substring(0, 4));
  else if (num.length >= 2) year = Number(num.substring(0, 2));
  else return -1;
  num = "";

  while ("0" > time[i] || time[i] > "9") i++;

  let month = 1;
  while (time[i] >= "0" && time[i] <= "9" && i < len) num += time[i++];
  month = Number(num);
  if (1 > month || month > 12) return -1;
  month--;
  num = "";

  while ("0" > time[i] || time[i] > "9") i++;

  let day = 1;
  while (time[i] >= "0" && time[i] <= "9" && i < len) num += time[i++];
  day = Number(num);
  if (1 > day || day > 31) return -1;
  num = "";

  while ("0" > time[i] || time[i] > "9") i++;

  let hour = 12;
  while (time[i] >= "0" && time[i] <= "9" && i < len) num += time[i++];
  hour = Number(num);
  if (0 > hour || hour > 23) return -1;
  num = "";

  while ("0" > time[i] || time[i] > "9") i++;

  let min = 0;
  while (time[i] >= "0" && time[i] <= "9" && i < len) num += time[i++];
  min = Number(num);
  if (0 > min || min > 59) return -1;

  const date = new Date(year, month, day, hour, min);

  const count = date.getTime() - Date.now();
  if (count > 0) return count;
  else return -1;
}
