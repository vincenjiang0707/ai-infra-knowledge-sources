# [Issue #50] The `/run` commands expose the use_followup parameter

source: https://github.com/gpu-mode/kernelbot/issues/50
state: closed | updated: 2024-12-21T20:26:19Z
labels: 

## 正文

The addition of the use_followup parameter causes the `/run` commands to expose it in Discord. I don't know if there is a way to hide it -- it's for internal use only. If we can't find a way to hide it, we may want to modify `verifyruns`.

## 评论 (3)

### alexzhang13 · 2024-12-13

I've dug around and generally I don't think it's possible.

What if we wrapped it in a try-except function instead? Something like the following:

```
def discord_followup_wrapper(interaction: discord.Interaction, msg: str) -> None:
    """
    To get around response messages in slash commands that are
    called externally, send a message using the followup.
    """
    try:
        await interaction.response.send_message(msg)

    except Exception:
        await interaction.followup.send(msg)
```

### b9r5 · 2024-12-15

Hey @alexzhang13. That idea might work. I had a comment on discord_followup_wrapper that I left in your other PR. Maybe we could get Siro's opinion on discord_followup_wrapper. 

One idea I had was to create "internal" functions that have the extra parameters, and then have the `/run` slash commands use function that do not have the extra parameters, but instead delegate to the functions that do have the extra parameters. The previous sentence isn't easy to follow :) so I put up a branch to explain what I mean: https://github.com/gpu-mode/discord-cluster-manager/tree/benh/use-followup-oops

I tested this idea out, and it does hide the `use_followup` parameter on Discord, and does not expose `internal_use_followup` on Discord.

### alexzhang13 · 2024-12-21

This is fixed now.
