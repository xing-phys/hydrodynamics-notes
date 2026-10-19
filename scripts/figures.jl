#!/usr/bin/env julia
# Reproducible analytic figures; requires CairoMakie for the PDF snapshots.
using CairoMakie

const root = dirname(@__DIR__)
const out = joinpath(root, "figs")
mkpath(out)
set_theme!(Theme(fontsize=15, font="DejaVu Sans", linewidth=2.3,
                 Axis=(xgridcolor=(:gray, 0.14), ygridcolor=(:gray, 0.14))))
teal = "#16776f"
ochre = "#bd8248"
f = Figure(size=(850, 1080), backgroundcolor=:white)
ax1 = Axis(f[1, 1], title="A  ·  Diffusion of a normalized Gaussian", xlabel="Position x", ylabel="Probability density")
x = range(-8, 8; length=500)
for (t, color) in zip((0, 1, 4, 8), ("#8ca59e", teal, ochre, "#79678b"))
    v = 1 + t # D = 1/2
    lines!(ax1, x, exp.(-x.^2 ./ (2v)) ./ sqrt(2π*v); color, label="t = $t")
end
axislegend(ax1; position=:rt, framevisible=false)
xlims!(ax1, -8, 8); ylims!(ax1, 0, 0.43)

ax2 = Axis(f[2, 1], title="B  ·  Two relaxing-current poles", xlabel="Re ω", ylabel="Im ω")
k = range(0, 2; length=501)
for (sign, color) in ((1, teal), (-1, ochre))
    ω = [-0.5im + sign*sqrt(complex(q*q - .25)) for q in k]
    lines!(ax2, real.(ω), imag.(ω); color, label=sign==1 ? "ω₊" : "ω₋")
    for q in (0.0, 0.3, 0.5, 1.0, 2.0)
        z = -0.5im + sign*sqrt(complex(q*q - .25))
        scatter!(ax2, [real(z)], [imag(z)]; color, markersize=8)
    end
end
axislegend(ax2; position=:rb, framevisible=false)
xlims!(ax2, -2.1, 2.1); ylims!(ax2, -1.1, 0.1)

ax3 = Axis(f[3, 1], title="C  ·  Gravity–capillary wave phase speed", xlabel="Dimensionless wave number q = kH", ylabel="Phase speed / √(gH)")
q = range(0.001, 20; length=500)
for (α, color) in zip((0, .001, .01, .1), ("#8ca59e", teal, ochre, "#79678b"))
    c = sqrt.((1 ./ q .+ α.*q) .* tanh.(q))
    lines!(ax3, q, c; color, label="α = $α")
end
axislegend(ax3; position=:rt, framevisible=false)
xlims!(ax3, 0, 20); ylims!(ax3, 0, 1.65)
save(joinpath(out, "laboratory.pdf"), f)
save(joinpath(out, "laboratory.png"), f; px_per_unit=1.5)

# Potential-flow streamlines around a circular cylinder: ψ/U = y(1-a²/r²).
open(joinpath(out, "flow.svg"), "w") do io
    println(io, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 330" role="img"><title>Potential-flow streamlines around a cylinder</title><desc>Illustrative inviscid streamlines avoid a circular obstacle. The analytic streamfunction is constant on each line.</desc>""")
    for c in vcat(collect(-2.4:0.25:-0.15), collect(0.15:0.25:2.4))
        points = String[]
        for x in range(-5, 5; length=350)
            lo = sqrt(max(0, .8^2-x^2)); hi = 5.0
            for _ in 1:55
                mid = (lo+hi)/2
                ψ = mid*(1-.8^2/(x*x+mid*mid))
                ψ < abs(c) ? (lo=mid) : (hi=mid)
            end
            y = sign(c)*(lo+hi)/2
            push!(points, "$(round(480+91x; digits=2)),$(round(165-60y; digits=2))")
        end
        opacity = .25 + .6*exp(-abs(c)/2)
        println(io, "<polyline points=\"$(join(points, " "))\" fill=\"none\" stroke=\"#3b9b8c\" stroke-width=\"1.5\" opacity=\"$opacity\"/>")
    end
    println(io, """<ellipse cx="480" cy="165" rx="72.8" ry="48" fill="#16776f" fill-opacity="0.07" stroke="#4c9c8a" stroke-width="1.5"/><text x="825" y="303" font-family="system-ui,sans-serif" font-size="11" fill="#708f83" letter-spacing="2">COLLECTIVE FLOW</text></svg>""")
end
println("Created flow.svg and laboratory.pdf/png")
