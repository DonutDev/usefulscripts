#wikipedia script
#!/bin/bash
wiki () {
        search_term="${1}"
        lynx https://en.wikipedia.org/wiki/${search_term}
}
