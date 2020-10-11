<script lang="ts">
    import type { PlayerModel } from "../../utils/models";
    export let player:PlayerModel;
</script>

<div class="player-container">
    <h1>{player.name}</h1>
    <div class="stats">
        <div class="health">
            <span>HP: {player.currentHP}/{player.hp}</span>
            <div class="progress-container">
                <div class="progress-placeholder" />
                <div class="progress" style="width: {player.currentHP/player.hp*100}%;" />
                <span class="progress-text">{(player.currentHP/player.hp*100).toFixed(2)}%</span>
            </div>
        </div>
        <div class="mana">
            <span>MP: {player.currentMana}/{player.mana}</span>
            <div class="progress-container">
                <div class="progress-placeholder" />
                <div class="progress" style="width: {player.currentMana/player.mana*100}%;" />
                <span class="progress-text">{(player.currentMana/player.mana*100).toFixed(2)}%</span>
            </div>
        </div>
    </div>
    <div class="image-container">
        <img class="player" src="assets/images/besta.png" alt="besta"/>
    </div>
</div>

<style lang="scss">
    .player-container{
        display: flex;
        background-color: #303030;
        flex-direction: column;
        flex: 1 1 auto;
        padding: 20px;

        h1{
            text-align: center;
        }

        .health{
            color: red;
            margin-bottom: 10px;

            .progress{
                background-color: red;
            }
        }

        .mana{
            color: cornflowerblue;

            .progress{
                background-color: cornflowerblue;
            }
        }

        .progress-container{
            width: 100%;
            height: 20px;
            position: relative;

            .progress{
                height: 100%;
                border-radius: 10px;
                transition: width 0.5s;
            }

            .progress-text{
                color: white;
                position: absolute;
                top: 0;
                right: 50%;
                transform: translate(50%);
            }

            .progress-placeholder{
                height: 100%;
                width: 100%;
                border-radius: 10px;
                background-color: #222222;
                margin-bottom: -20px;
            }
        }

        .image-container{
            display: flex;
            justify-content: center;
            align-items: center;      
            height: 100%;  
            
            .player{
                max-width: 20vw;
            }
        }
    }
</style>