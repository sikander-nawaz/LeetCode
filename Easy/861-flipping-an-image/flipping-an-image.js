/**
 * @param {number[][]} image
 * @return {number[][]}
 */
var flipAndInvertImage = function (image) {
  for (let i = 0; i < image.length; i++) {
    image[i] = image[i].reverse();
    if (image[i]) {
      image[i] = image[i].map((item) => (item === 0 ? 1 : 0));
    }
  }
  return image;
};