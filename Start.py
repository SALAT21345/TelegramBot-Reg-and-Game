import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import keyboard as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types.web_app_info import WebAppInfo
adminid = '1243576393'
class Reg(StatesGroup):
    Steam_Link = State()
    InfoForPeople = State()
    Get_Photo_Games = State()
    Get_Akk_DS = State()

bot = Bot(token='7052647638:AAGzBpl65HjA0olywqzsQHt7pNH0cD9LNUQ')
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!")
    await message.answer("Выберите подходящее для вас действие.", reply_markup=kb.main)


@dp.message(Command('Сайт'))
async def Site(message: Message):
    await message.answer("Конечно, вот наш сайт!", reply_markup=kb.urls)


@dp.message(Command('/Game'))
async def game(message:Message):
    await message.answer("Кликай, что бы открыть!", web_app=WebAppInfo() )

@dp.message(Command('Регистрация'))
async def Site(message: Message, state: FSMContext):
    await state.set_state(Reg.Steam_Link)
    await message.answer("Вы выбрали 'Регистрация'. Перед подачей заявки на вступление в команду отправьте, пожалуйста, ссылку на ваш Стим аккаунт.")

@dp.message(Command('/Game'))
async def game(message:Message):
    await message.answer("Кликай, что бы открыть!" )

@dp.message(Reg.Steam_Link)
async def SaveLink(message: Message, state: FSMContext):
    await state.update_data(Steam_Link = message.text)
    await state.set_state(Reg.InfoForPeople)
    await message.answer('Опишите себя как человека, а также как тимейта.')


@dp.message(Reg.InfoForPeople)
async def GetInfoForPeople(message:Message, state:FSMContext):
    await state.update_data(InfoForPeople = message.text)
    await state.set_state(Reg.Get_Photo_Games)
    await message.answer("Отправьте фото из 'Последние матчи' с вашими победами/поражениями.")



@dp.message(Reg.Get_Photo_Games)
async def SavePhotoGame(message: Message, state: FSMContext):
    photo = message.photo[-1].file_id
    await state.update_data(Get_Photo_Games = photo)
    await state.set_state(Reg.Get_Akk_DS)
    await message.answer("Ваш дискорд: ")


@dp.message(Reg.Get_Akk_DS)
async def saveds(message: Message, state: FSMContext):
    await state.update_data(Get_Akk_DS = message.text)
    dataForUser = await state.get_data()
    await message.answer('Отлично. Вы прошли регистрацию, ожидайте ответа в течении дня.\n Обычно ответ приходит в течении часа, но иногда могут быть задержки.')
    await state.clear()
    await bot.send_message(adminid, f'Стим: {dataForUser["Steam_Link"]}\nОписание: {dataForUser["InfoForPeople"]}\nДискорд:{dataForUser["Get_Akk_DS"]}\nФото матчей:')
    await bot.send_photo(adminid, dataForUser["Get_Photo_Games"])


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())