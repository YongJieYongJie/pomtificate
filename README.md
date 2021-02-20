# POMtificate

_sbt POMtified!_

POMtificate generates a [pom.xml][pom-link] for your [Play
Framework][play-framework-link] project, allowing you to enjoy coding in VS
Code, Vim, Neovim, or any other editors / IDE that uses the [eclipse.jdt.ls
language server][eclipse-lang-server-link].

[pom-link]: https://maven.apache.org/guides/introduction/introduction-to-the-pom.html
[play-framework-link]: https://www.playframework.com/
[eclipse-lang-server-link]: https://github.com/eclipse/eclipse.jdt.ls


# Installation and Usage

1. Clone this Git repository anywhere accessible on your system.
1. Change into the root directory of your Play Framework project (i.e., the
   directory containing the `build.sbt` file).
1. Run `<path-to-pomtificate-git-repository>/what-the-pom`, and let the
   magic happen. (You may need to run `chmod u+x
   <path-to-pomtificate-git-repository>/what-the-pom` to make the script
   executable first.)


# Limitations

1. Currently the script is only tested on Play Framework version 2.5 and Java 1.8.


# Troubleshooting

[Work-in-Progress] For now, refer to the blog post at
https://yongjie.codes/guides/java-play-sbt-on-vscode/.
