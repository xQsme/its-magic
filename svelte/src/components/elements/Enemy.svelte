<script lang="ts">
    export let enemy:Enemy;
</script>

<div class="container">
    <div class="stats">
        <div class="container2">
            <img src="./assets/images/health.png">
            <div class="centered" style="color: red">{enemy.hp}/{enemy.hp}</div>
        </div>
        <div class="container2">
            <img src="./assets/images/mana.png">
            <div class="centered" style="color: cornflowerblue">{enemy.time}/{enemy.time}</div>
        </div>
    </div>
    <div class="enemy-container">
        <img class="enemy" src={enemy.image} alt="enemy"/>
    </div> 
</div>
     
<style lang="scss">
    .container{
        display: flex;
        background-color: #303030;
        flex-direction: column;
        flex: 1 1 auto;
        padding: 20px;

        .stats{
            display: flex;
        }

        .container2 {
            position: relative;
            text-align: center;
            width: 50%;

            img{
                max-width: 300px;
                width: 100%;
            }
            
            .centered {
                position: absolute;
                top: 72.5%;
                left: 62%;
                transform: translate(-50%, -50%);
                font-size: 20px;
            }

        }
        .enemy-container{
            display: flex;
            justify-content: center;
            align-items: center;      
            height: 100%;  
            
            .enemy{
                max-width: 25vw;
            }
        }
    }


    

</style>