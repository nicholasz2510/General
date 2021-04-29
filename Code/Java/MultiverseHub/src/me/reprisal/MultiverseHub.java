package me.reprisal;

import org.bukkit.World;
import org.bukkit.Location;
import org.bukkit.ChatColor;
import org.bukkit.entity.Player;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.Bukkit;
import org.bukkit.permissions.Permission;
import org.bukkit.plugin.java.JavaPlugin;

public class MultiverseHub extends JavaPlugin
{
    public Permission playerPermission;

    public MultiverseHub() {
        this.playerPermission = new Permission("hub.allow");
    }

    public void onEnable() {
        Bukkit.getServer().getPluginManager().addPermission(this.playerPermission);
    }

    public boolean onCommand(final CommandSender sender, final Command cmd, final String commandLabel, final String[] args) {
        if (!(sender instanceof Player)) {
            sender.sendMessage(ChatColor.RED + "This plugin is for players only!");
            return true;
        }
        final Player p = (Player)sender;
        if (p.hasPermission("hub.allow") && cmd.getName().equalsIgnoreCase("sethub")) {
            this.getConfig().set("spawn.world", (Object)p.getLocation().getWorld().getName());
            this.getConfig().set("spawn.x", (Object)p.getLocation().getX());
            this.getConfig().set("spawn.y", (Object)p.getLocation().getY());
            this.getConfig().set("spawn.z", (Object)p.getLocation().getZ());
            this.getConfig().set("spawn.yaw", (Object)p.getLocation().getYaw());
            this.getConfig().set("spawn.pitch", (Object)p.getLocation().getPitch());
            this.saveConfig();
            p.sendMessage(ChatColor.GREEN + "The Hub has been successfully set!");
            return true;
        }
        if (cmd.getName().equalsIgnoreCase("Hub")) {
            if (this.getConfig().getConfigurationSection("spawn") == null) {
                p.sendMessage(ChatColor.RED + "The Hub has not been set!");
                return true;
            }
            final World w = Bukkit.getServer().getWorld(this.getConfig().getString("spawn.world"));
            final double x = this.getConfig().getDouble("spawn.x");
            final double y = this.getConfig().getDouble("spawn.y");
            final double z = this.getConfig().getDouble("spawn.z");
            final float yaw = (float)this.getConfig().getInt("spawn.yaw");
            final float pitch = (float)this.getConfig().getInt("spawn.pitch");
            p.teleport(new Location(w, x, y, z, yaw, pitch));
            p.teleport(new Location(w, x, y, z, yaw, pitch));
            p.sendMessage(ChatColor.GREEN + "You have been successfully teleported the the Hub!");
        }
        return true;
    }
}
