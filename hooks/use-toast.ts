import * as React from "react"

type ToastActionElement = React.ReactElement

export interface Toast {
  id: string
  title?: string
  description?: string
  action?: ToastActionElement
  variant?: "default" | "destructive"
}

type ToasterToast = Toast & {
  id: string
  open: boolean
  onOpenChange: (open: boolean) => void
}

const TOAST_LIMIT = 5
const TOAST_REMOVE_DELAY = 5000

let count = 0

function genId() {
  count = (count + 1) % Number.MAX_VALUE
  return count.toString()
}

type ActionType = {
  type: "ADD_TOAST" | "UPDATE_TOAST" | "DISMISS_TOAST" | "REMOVE_TOAST"
  toast?: Partial<ToasterToast>
  toastId?: string
}

const toastTimeouts = new Map<string, ReturnType<typeof setTimeout>>()

const addToRemoveQueue = (toastId: string) => {
  if (toastTimeouts.has(toastId)) {
    return
  }

  const timeout = setTimeout(() => {
    toastTimeouts.delete(toastId)
    dispatch({
      type: "REMOVE_TOAST",
      toastId: toastId,
    })
  }, TOAST_REMOVE_DELAY)

  toastTimeouts.set(toastId, timeout)
}

export const reducer = (state: ToasterToast[], action: ActionType): ToasterToast[] => {
  switch (action.type) {
    case "ADD_TOAST":
      return [{ ...action.toast, id: genId(), open: true, onOpenChange: () => {} } as ToasterToast, ...state].slice(
        0,
        TOAST_LIMIT
      )

    case "UPDATE_TOAST":
      return state.map((t) =>
        t.id === action.toast?.id ? { ...t, ...action.toast } : t
      )

    case "DISMISS_TOAST": {
      const { toastId } = action

      if (toastId) {
        addToRemoveQueue(toastId)
      } else {
        state.forEach((toast) => {
          addToRemoveQueue(toast.id)
        })
      }

      return state.map((t) =>
        t.id === toastId || toastId === undefined
          ? {
              ...t,
              open: false,
            }
          : t
      )
    }
    case "REMOVE_TOAST":
      if (action.toastId === undefined) {
        return []
      }
      return state.filter((t) => t.id !== action.toastId)
  }
}

const listeners: Array<(state: ToasterToast[]) => void> = []

let memoryState: ToasterToast[] = []

function dispatch(action: ActionType) {
  memoryState = reducer(memoryState, action)
  listeners.forEach((listener) => {
    listener(memoryState)
  })
}

export function toast({ ...props }: Omit<Toast, "id">) {
  const id = genId()

  const update = (props: Partial<Toast>) =>
    dispatch({
      type: "UPDATE_TOAST",
      toast: { ...props, id },
    })
  const dismiss = () => dispatch({ type: "DISMISS_TOAST", toastId: id })

  dispatch({
    type: "ADD_TOAST",
    toast: {
      ...props,
      id,
      open: true,
      onOpenChange: (open: boolean) => {
        if (!open) dismiss()
      },
    },
  })

  return {
    id: id,
    dismiss,
    update,
  }
}

export function useToast() {
  const [state, setState] = React.useState<ToasterToast[]>(memoryState)

  React.useEffect(() => {
    listeners.push(setState)
    return () => {
      const index = listeners.indexOf(setState)
      if (index > -1) {
        listeners.splice(index, 1)
      }
    }
  }, [state])

  return {
    ...state[0],
    toast,
    dismiss: (toastId?: string) => dispatch({ type: "DISMISS_TOAST", toastId }),
  }
}
