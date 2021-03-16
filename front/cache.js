const isServer = typeof window === 'undefined'
const storage = !isServer ? window.localStorage : null

function serialize (val) {
  return JSON.stringify(val)
}

function deserialize (val) {
  if (typeof val !== 'string') {
    return undefined
  }
  try {
    return JSON.parse(val)
  } catch (e) {
    return val || undefined
  }
}
function set (key, val) {
    storage.setItem(key, serialize(val))
    return val
}
function get (key, def) {
    let val = deserialize(storage.getItem(key))
    return (val === undefined ? def : val)
}
