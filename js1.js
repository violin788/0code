val = "https://www.youtube.com/watch?v=OLNz0313A4k"
eqa = val.search("=")
sub = val.substring(eqa+1,val.length);
y2m = "https://www.y2mate.com/youtube/"+sub

ray = []
ray.push(val)
ray.push(eqa)
ray.push(sub)
ray.push(y2m)
console.log(y2m)