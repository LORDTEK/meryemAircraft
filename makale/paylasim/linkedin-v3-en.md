In Section 8 of our paper we listed, in four items, where our own results could
most efficiently be attacked. The intent was simple: say it before someone else
has to.

We have now carried out the first of those four.

Our weakest number was the zero-lift drag, and we knew where the weakness sat —
we were treating a twenty-five percent thick centre body as a two-dimensional
section. A three-dimensional solution removes that assumption.

**The result went against us.** The drag is nine percent above what the strip
method gave. The margin on our assumption narrowed from seventeen percent to
eleven.

The assumption still holds. But what matters to us is not the number itself —
it is that its uncertainty is **measured**: three grids, four wall resolutions,
two turbulence models. The dominant term turned out to be the turbulence model,
not the grid.

One thing worth passing on. **Residuals can lie.** At a velocity residual of
1.6×10⁻⁵ our computed drag was still fifty-five percent above its converged
value. Had we stopped there, we would have reported it half again too high.

What we could not do: the transition model would not converge, so the
clean-surface case remains untested. That is written down too.

The repository holds not only the results but a measured record of every
hypothesis that failed along the way.

📄 doi.org/10.5281/zenodo.22144194 (v3)
💻 github.com/LORDTEK/meryemAircraft
