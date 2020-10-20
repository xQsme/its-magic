export interface AuthModel {
	email:string,
	username:string,
	role:string[],
    token:string,
}

export interface EnemyModel{
    id:number,
    name:string,
    xp:number,
    hp:number,
    currentHP:number,
    mana:number,
    currentMana:number,
    damage:number,
    image:string,
    sound:string,
}

export interface SpellModel{
    id:number,
    name:string,
    damage:number,
    image:string,
    colors:ColorModel[],
}

export interface ColorModel{
    id:number,
    name:string,
    hexa:string,
}

export interface PlayerModel{
    id:number,
    name:string,
    xp:number,
    currentXP:number,
    hp:number,
    currentHP:number,
    mana:number,
    currentMana:number,
    image:string,
    sound:string,
}