// This Pine Script® code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Tips2Wealth
//@version=6
indicator("Parabolic SAR", overlay=true)

//ta.study(title="MA Cross", overlay=true, resolution="")
short = ta.sma(close, 7)
medium = ta.sma(close,25)
long = ta.sma(close, 99)
////mySAR = sar(0,20,25)
plot(short, color = color.red)
plot(medium, color = color.rgb(230, 255, 2), linewidth = 2)
plot(long, color = color.green, linewidth = 3)
///plot(long, color = color.yellow)
//plot(cross(short, long) ? long : na, style = plot.style_cross, linewidth = 4, color = color.orange )
plot( ta.cross(short,medium) ? short : na , style = plot.style_cross, linewidth = 9, color = short > medium ? #91cc51 : #ff9898 )

/// We Must use ta. before sma() to avoid errors in V6 !!!!!!!!!!
//MA_Value = ta.sma(close,25)
// SAR settings
start = input.float(0.02, title="Start", step=0.01)
increment = input.float(0.02, title="Increment", step=0.01)
maximum = input.float(0.20, title="Maximum", step=0.01)

// Calculate SAR
SAR_Value = ta.sar(start, increment, maximum)


// Display SAR dots
plot(SAR_Value, title="Parabolic SAR", style=plot.style_circles,  color= short>SAR_Value? color.green : color.red, linewidth=4)
