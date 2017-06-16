# BespON syntax highlighting for VS Code

This is an extension for [VS Code](https://code.visualstudio.com/) that
provides syntax highlighting for [BespON](https://bespon.org/).  It is
available through the Visual Studio Marketplace, and thus may be installed
with the VS Code extension manager.

A simple installation script `install.py` is provided to automate manual
installation of development versions.


<div style="display: inline-block;overflow-x: auto;width: 100%;padding: 1em;color: #d4d4d4;background-color: #1e1e1e;font-family: Consolas, 'Courier New', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><span style="color: #608b4e;"># Line comments are allowed!  They can always be round-tripped as long as data</span></div><div><span style="color: #608b4e;"># elements are only modified, not added or removed.</span></div><br><div><span style="color: #608b4e;">### This is a doc comment.  It can always be round-tripped.###</span></div><div><span style="color: #608b4e;"># Only one doc comment is allowed per data element; another couldn't be here.</span></div><br><div><span style="color: #ce9178;">"quoted key with \x5C escapes"</span><span style="color: #d4d4d4;"> = </span><span style="color: #ce9178;">'quoted value with \u{5C} escapes'</span></div><br><div><span style="color: #ce9178;">`literal key without \ escapes`</span><span style="color: #d4d4d4;"> = </span><span style="color: #ce9178;">``literal value without `\` escapes``</span></div><br><div><span style="color: #608b4e;"># ASCII identifier-style strings are allowed unquoted.</span></div><div><span style="color: #608b4e;"># Unquoted Unicode identifiers can optionally be enabled.</span></div><div><span style="color: #ce9178;">unquoted_key</span><span style="color: #d4d4d4;"> = </span><span style="color: #ce9178;">unquoted_value</span></div><br><div><span style="color: #ce9178;">inline_dict</span><span style="color: #d4d4d4;"> = {</span><span style="color: #ce9178;">key1</span><span style="color: #d4d4d4;"> = </span><span style="color: #ce9178;">value1</span><span style="color: #d4d4d4;">, </span><span style="color: #ce9178;">key2</span><span style="color: #d4d4d4;"> = </span><span style="color: #ce9178;">value2</span><span style="color: #d4d4d4;">,}  </span><span style="color: #608b4e;"># Trailing commas are fine.</span></div><br><div><span style="color: #ce9178;">inline_list_of_ints</span><span style="color: #d4d4d4;"> = [</span><span style="color: #b5cea8;">1</span><span style="color: #d4d4d4;">, </span><span style="color: #569cd6;">0x</span><span style="color: #b5cea8;">12</span><span style="color: #d4d4d4;">, </span><span style="color: #569cd6;">0o</span><span style="color: #b5cea8;">755</span><span style="color: #d4d4d4;">, </span><span style="color: #569cd6;">0b</span><span style="color: #b5cea8;">1010</span><span style="color: #d4d4d4;">]  </span><span style="color: #608b4e;"># Hex, octal, and binary!</span></div><br><div><span style="color: #ce9178;">list_of_floats</span><span style="color: #d4d4d4;"> =</span></div><div><span style="color: #d4d4d4;">  * </span><span style="color: #b5cea8;">1.2e3</span></div><div><span style="color: #d4d4d4;">  * </span><span style="color: #b5cea8;">-inf</span><span style="color: #d4d4d4;">  </span><span style="color: #608b4e;"># Full IEEE 754 compatibility.  Infinity and NaN are not excluded.</span></div><div><span style="color: #d4d4d4;">  * </span><span style="color: #569cd6;">0x</span><span style="color: #b5cea8;">4.3p2</span><span style="color: #d4d4d4;">  </span><span style="color: #608b4e;"># Hex floats, to avoid rounding issues.</span></div><br><div><span style="color: #ce9178;">wrapped_string</span><span style="color: #d4d4d4;"> = </span><span style="color: #ce9178;">"""string containing no whitespace lines in which line breaks</span></div><div><span style="color: #ce9178;">    are replaced with spaces, and "quotes" are possible by via delimiters"""</span></div><br><div><span style="color: #ce9178;">multiline_literal_string</span><span style="color: #d4d4d4;"> = </span><span style="color: #ce9178;">|```</span></div><div><span style="color: #ce9178;">        A literal string in which linebreaks are kept (as '\n')</span></div><div><span style="color: #ce9178;">        and leading indentation (relative to delimiters) is preserved,</span></div><div><span style="color: #ce9178;">        with special delimiters always on lines by themselves.</span></div><div><span style="color: #ce9178;">    |```/</span></div><br><div><span style="color: #ce9178;">multiline_escaped_string</span><span style="color: #d4d4d4;"> = </span><span style="color: #ce9178;">|"""</span></div><div><span style="color: #ce9178;">    The same idea as the literal string, but with backslash escapes.</span></div><div><span style="color: #ce9178;">    |"""/</span></div><br><div><span style="color: #ce9178;">key1</span><span style="color: #d4d4d4;">.</span><span style="color: #ce9178;">key2</span><span style="color: #d4d4d4;"> = </span><span style="color: #569cd6;">true</span><span style="color: #d4d4d4;">  </span><span style="color: #608b4e;"># Key path style; same as "key1 = {key2 = true}"</span></div><br><div><span style="color: #d4d4d4;">|=== </span><span style="color: #ce9178;">section</span><span style="color: #d4d4d4;">.</span><span style="color: #ce9178;">subsection</span><span style="color: #d4d4d4;">  </span><span style="color: #608b4e;"># Same as "section = {subsection = {key = value}}"</span></div><div><span style="color: #ce9178;">key</span><span style="color: #d4d4d4;"> = </span><span style="color: #ce9178;">value</span></div><div><span style="color: #d4d4d4;">|===/  </span><span style="color: #608b4e;"># Back to root level.  Can be omitted if sections never return to root.</span></div><br></div>
